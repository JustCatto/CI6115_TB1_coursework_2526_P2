package q4;

public class InventoryManagement implements Observer {

  private static InventoryManagement instance;

  private InventoryManagement() {}

  public static InventoryManagement getInstance() {
    if (instance == null) {
      instance = new InventoryManagement();
    }
    return instance;
  }

  public void update() {
    System.out.println("Updating inventory...");
  }
}
