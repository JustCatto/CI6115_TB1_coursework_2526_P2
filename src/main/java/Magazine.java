public class Magazine extends Item {

  private int Pages;
  private String Publisher;

  public Magazine(
          String name,
          float price,
          String description,
          String code,
          ProductPhoto[] productPhotos,
          int pages,
          String publisher) {
    super(name, price, description, code, productPhotos);
    Pages = pages;
    Publisher = publisher;
  }

  public Magazine(String name, float price, String description, String code, ProductPhoto[] productPhotos) {
    super(name, price, description, code, productPhotos);
    Pages = 0;
    Publisher = "John Doe";
  }


  public int getPages() {
    return Pages;
  }

  public void setPages(int pages) {
    Pages = pages;
  }

  public String getPublisher() {
    return Publisher;
  }

  public void setPublisher(String publisher) {
    Publisher = publisher;
  }
}
