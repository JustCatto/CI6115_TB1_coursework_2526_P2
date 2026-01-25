public class NotebookFactory implements Factory {

    public Item createItem(String name, float price, String description, String code, Photo[] productPhotos) {
        return new Notebook(
                name,
                price,
                description,
                code,
                productPhotos
        );
    }
}
