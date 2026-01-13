import java.util.List;

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

interface ShapeFactory {

  Shape createShape();
}

class CircleFactory implements ShapeFactory {

  public Shape createShape() {
    return new Circle();
  }
}

class BoxFactory implements ShapeFactory {

  public Shape createShape() {
    return new Box();
  }
}

class TriangleFactory implements ShapeFactory {

  public Shape createShape() {
    return new Triangle();
  }
}

class Overriding {

  public static void main(String[] args) {
    List<ShapeFactory> factories =
        List.of(new BoxFactory(), new TriangleFactory(), new CircleFactory());
    for (ShapeFactory factory : factories) {
      Shape shape = factory.createShape();
      shape.numberOfSides();
      shape.draw();
    }
  }
}
