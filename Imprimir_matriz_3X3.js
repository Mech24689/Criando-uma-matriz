const matriz = [[1,2,3],[4,5,6],[7,8,9]]
let array = []
for(let li = 0; li < 3; li++){
    for(let col = 0; col < 3; col++){
        array.push(matriz[li][col])
    }
    console.log(array)
    while(array != 0){
        array.pop()
    }
}