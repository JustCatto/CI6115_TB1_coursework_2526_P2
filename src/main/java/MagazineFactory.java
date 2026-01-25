public class MagazineFactory implements Factory {

    public Item createItem(String name, float price, String description, String code, Photo[] productPhotos) {
        return new Magazine(
                name,
                price,
                description,
                code,
                productPhotos
        );
    }
}
