if ("2" in info.treedecs) { info.treedecs["2"].dot = `
graph {
bgcolor=transparent
edge [color="#ff8c00b2"]
b2 [label="1", fillcolor="#ff8c00b2"]
b3 [label="1", fillcolor="#ff8c00b2"]
b1 [label="2, 3", fillcolor="#ff8c00b2"]
b1 -- b2
b1 -- b3
}
`}
