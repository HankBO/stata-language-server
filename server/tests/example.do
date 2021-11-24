gen x = 3
replace x= 10
gen y = "1 + 3" //1+3
foreach x of varlist {
    gen a_`x' = 1
    forvalue i = 1/2 {
            display `i'
    }
}
