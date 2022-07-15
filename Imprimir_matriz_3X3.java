public class Imprimir_matriz_3X3{
    public static void main(String[] args) {
        int matriz[][] = {{1,2,3},{4,5,6},{7,8,9}};
        for(int li = 0; li < 3; li++){
            for(int col = 0; col < 3; col++){
                System.out.print(matriz[li][col] + " ");
            }
            System.out.println("");
        }
    }
}