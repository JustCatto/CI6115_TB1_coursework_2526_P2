public class BookFactory implements Factory {

    public Item createItem(String name, float price, String description, String code, Photo[] productPhotos) {
        return new Book(
                name,
                price,
                description,
                code,
                productPhotos
        );
    }
}
