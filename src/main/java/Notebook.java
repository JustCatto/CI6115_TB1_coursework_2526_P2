public class Notebook extends Item {

  private String size;
  private int pages;

  public Notebook(
          String name,
          float price,
          String description,
          String code,
          Photo[] productPhotos,
          String size,
          int pages) {
    super(name, price, description, code, productPhotos);
    this.size = size;
    this.pages = pages;
  }

  public Notebook(String name, float price, String description, String code, Photo[] productPhotos) {
    super(name, price, description, code, productPhotos);
  }

  public String getSize() {
    return size;
  }

  public void setSize(String size) {
    this.size = size;
  }

  public int getPages() {
    return pages;
  }

  public void setPages(int pages) {
    this.pages = pages;
  }
}
