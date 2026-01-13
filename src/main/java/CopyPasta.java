class Shape {
  void draw() {
    System.out.println("Mention shape here");
  }

  void numberOfSides() {
    System.out.println("side = 0");
  }
}

class Circle extends Shape {

  void draw() {
    System.out.println("CIRCLE ");
  }

  void numberOfSides() {
    System.out.println("side = 0 ");
  }
}

class Box extends Shape {

  void draw() {
    System.out.println("BOX ");
  }

  void numberOfSides() {
    System.out.println("side= 6");
  }
}

class Triangle extends Shape {
  void draw() {
    System.out.println("TRIANGLE ");
  }

  void numberOfSides() {
    System.out.println("side = 3 ");
  }
}

class Overriding {

  public static void main(String[] args) {
  }
}
