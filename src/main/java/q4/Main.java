package q4;

public class Main {

  public static void main(String[] args) {
    OrderProcessor orderProcessor = OrderProcessor.getInstance();

    orderProcessor.addObserver(EmailSystem.getInstance());
    orderProcessor.addObserver(InventoryManagement.getInstance());
    orderProcessor.addObserver(OrderTracking.getInstance());

    orderProcessor.processOrder();
  }
}
