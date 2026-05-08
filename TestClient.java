public class TestClient {
    public static void main(String[] args) {

        AiServiceClient client = new AiServiceClient();

        String response = client.generate("What is AI?");
        System.out.println("Response: " + response);
    }
}