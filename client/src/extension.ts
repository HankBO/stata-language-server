/* -------------------------------------------------------------------------
 * Original work Copyright (c) Microsoft Corporation. All rights reserved.
 * Original work licensed under the MIT License.
 * See ThirdPartyNotices.txt in the project root for license information.
 * All modifications Copyright (c) Open Law Library. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License")
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http: // www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ----------------------------------------------------------------------- */
"use strict";

import * as net from "net";
import * as path from "path";
import { ExtensionContext, ExtensionMode, workspace, window } from "vscode";
import { LanguageClient, LanguageClientOptions, ServerOptions } from "vscode-languageclient/node";
import * as child_process from "child_process";

/**
 * Check if pygls is already installed on this python.
 *
 * @param python path of the python interpreter
 */
 function ispyglsInstalled(python: string): boolean {
  try {
    child_process.execFileSync(python, ["-c", "import pygls"]);
    return true;
  } catch {
    return false;
  }
}

/**
 * Check if python version looks supported.
 *
 * @param python path of the python interpreter
 */
 function isPythonVersionCompatible(python: string): boolean {
  try {
    child_process.execFileSync(python, [
      "-c",
      "import sys; sys.exit(sys.version_info[:2] < (3, 6))"
    ]);
    return true;
  } catch {
    return false;
  }
}

async function shortDelay() {
  return new Promise(resolve => setTimeout(resolve, 3000));
}

let client: LanguageClient;

function getClientOptions(): LanguageClientOptions {
  return {
    // Register the server for plain text documents
    documentSelector: [
      { scheme: "file", language: "stata" },
      { scheme: "untitled", language: "stata" },
    ],
    outputChannelName: "[pygls] StataLanguageServer",
    synchronize: {
      // Notify the server about file changes to '.clientrc files contain in the workspace
      fileEvents: workspace.createFileSystemWatcher("**/.clientrc"),
    },
  };
}

function startLangServerTCP(addr: number): LanguageClient {
  const serverOptions: ServerOptions = () => {
    return new Promise((resolve /*, reject */) => {
      const clientSocket = new net.Socket();
      clientSocket.connect(addr, "127.0.0.1", () => {
        resolve({
          reader: clientSocket,
          writer: clientSocket,
        });
      });
    });
  };

  return new LanguageClient(`tcp lang server (port ${addr})`, serverOptions, getClientOptions());
}

function startLangServer(
  command: string, args: string[], cwd: string,
): LanguageClient {
  const serverOptions: ServerOptions = {
    args,
    command,
    options: { cwd },
  };

  return new LanguageClient(command, serverOptions, getClientOptions());
}

export async function activate(context: ExtensionContext): Promise<void> {
  if (context.extensionMode === ExtensionMode.Development) {
    // Development - Run the server manually
    client = startLangServerTCP(2087);
  } else {
    // Production - Client is going to run the server (for use within `.vsix` package)
    const cwd = path.join(__dirname, "..", "..");
    const pythonPath = workspace.getConfiguration("python").get<string>("pythonPath");

    if (!pythonPath) {
      throw new Error("`python.pythonPath` is not set");
    }

    client = startLangServer(pythonPath, ["-m", "server"], cwd);

    if (!isPythonVersionCompatible(pythonPath)) {
      window.showErrorMessage(
        "Stata Language Server: Invalid python version, needs python >= 3.6"
      );
      return;
    }

    let setupSucceed = ispyglsInstalled(pythonPath);
    if (!setupSucceed) {
      const terminal = window.createTerminal("stata-ls");
      terminal.show(false);
      terminal.sendText(
        "# Install pygls on selected python.\n"
      );
      terminal.sendText(
        `${pythonPath} -m pip install --user -r "${cwd}/requirements.txt"`
      );
      for (let retries = 0; retries < 5; retries++) {
        await shortDelay();
        setupSucceed = ispyglsInstalled(pythonPath);
        if (setupSucceed) {
          break;
        }
      }
      if (setupSucceed) {
        window.showInformationMessage(
          "Stata Language Server: pygls installed"
        );
      } else {
        window.showErrorMessage(
          "Stata Language Server: Could not install pygls"
        );
      }
    }
  }

  context.subscriptions.push(client.start());
}

export function deactivate(): Thenable<void> {
  return client ? client.stop() : Promise.resolve();
}
