package q4;

abstract class Observable {
  Observer[] observers; // NEVER. AGAIN. AM I. USING. ARRAYS.
  int size;

  public Observable() {
    observers = new Observer[1];
    size = 0;
  }

  protected void notifyObservers() {
    for (int i = 0; i < size; i++) {
      observers[i].update();
    }
  }

  private void expandObserverArr() {
    int newSize = observers.length << 1;
    Observer[] newArr = new Observer[newSize];
    System.arraycopy(observers, 0, newArr, 0, size);
    observers = newArr;
  }

  void addObserver(Observer toAdd) {
    if (size >= observers.length) {
      expandObserverArr();
    }
    observers[size] = toAdd;
    size++;
  }

  void removeObserver(Observer toRemove) {
    for (int i = 0; i < size; i++) {
      Observer observer = observers[i];
      if (observer == toRemove) {
        observers[i] =
            observers[size - 1]; // Lil o(1) trick to remove from arrays, swap with last element,
        observers[size - 1] = null; // Then nuke last element. YAY!
        size--; // WHY DID I DECIDE TO IMPLEMENT THIS MANUALLY
        return; // We're done here
      }
    }
  }
}

interface Observer {
  void update();
}

public class OrderProcessor extends Observable {

  private static OrderProcessor instance;

  private OrderProcessor() {}

  public static OrderProcessor getInstance() {
    if (instance == null) {
      instance = new OrderProcessor();
    }
    return instance;
  }

  public void processOrder() {
    System.out.println("OrderSystem recieved order!");
    notifyObservers();
  }
}
