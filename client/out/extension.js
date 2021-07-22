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
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const net = require("net");
const path = require("path");
const vscode_1 = require("vscode");
const vscode_languageclient_1 = require("vscode-languageclient");
let client;
function getClientOptions() {
    return {
        // Register the server for plain text documents
        documentSelector: [
            { scheme: "file", language: "stata" },
            { scheme: "untitled", language: "stata" },
        ],
        outputChannelName: "[pygls] StataLanguageServer",
        synchronize: {
            // Notify the server about file changes to '.clientrc files contain in the workspace
            fileEvents: vscode_1.workspace.createFileSystemWatcher("**/.clientrc"),
        },
    };
}
function isStartedInDebugMode() {
    return process.env.VSCODE_DEBUG_MODE === "true";
}
function startLangServerTCP(addr) {
    const serverOptions = () => {
        return new Promise((resolve, reject) => {
            const clientSocket = new net.Socket();
            clientSocket.connect(addr, "127.0.0.1", () => {
                resolve({
                    reader: clientSocket,
                    writer: clientSocket,
                });
            });
        });
    };
    return new vscode_languageclient_1.LanguageClient(`tcp lang server (port ${addr})`, serverOptions, getClientOptions());
}
function startLangServer(command, args, cwd) {
    const serverOptions = {
        args,
        command,
        options: { cwd },
    };
    return new vscode_languageclient_1.LanguageClient(command, serverOptions, getClientOptions());
}
function activate(context) {
    if (isStartedInDebugMode()) {
        // Development - Run the server manually
        client = startLangServerTCP(2087);
    }
    else {
        // Production - Client is going to run the server (for use within `.vsix` package)
        const cwd = path.join(__dirname, "..", "..");
        const pythonPath = vscode_1.workspace.getConfiguration("python").get("pythonPath");
        if (!pythonPath) {
            throw new Error("`python.pythonPath` is not set");
        }
        client = startLangServer(pythonPath, ["-m", "server"], cwd);
    }
    context.subscriptions.push(client.start());
}
exports.activate = activate;
function deactivate() {
    return client ? client.stop() : Promise.resolve();
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map