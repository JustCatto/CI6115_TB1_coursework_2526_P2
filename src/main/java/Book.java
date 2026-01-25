public class Book extends Item {

  private int Pages;
  private String publisher;
  private Person[] authors;

  public Book(
          String name,
          float price,
          String description,
          String code,
          Photo[] productPhotos,
          int pages,
          String publisher,
          Person[] authors) {
    super(name, price, description, code, productPhotos);
    Pages = pages;
    this.publisher = publisher;
    this.authors = authors;
    if (authors.length == 0) {
      throw new IllegalArgumentException("Book must have at least 1 author.");
    }
  }

  public Book(String name, float price, String description, String code, Photo[] productPhotos) {
    super(name, price, description, code, productPhotos);
    this.publisher = "Unknown";
  }

}
