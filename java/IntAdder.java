public class IntAdder {
   private int x;
   private int y;
   private int z;
   IntAdder() {
      x = 39;
      y = 54;
      z = x + y;
   }
   public void printResults(){
      System.out.println("The value of 'z' is '" + z + "'");
   }

   public static void main(String[] args) {
      IntAdder ia = new IntAdder();
      ia.printResults();
   }
}
