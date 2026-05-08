import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class AiServiceClient {

    private static final String BASE_URL = "http://127.0.0.1:5000";

    // ✅ Health check (GET)
    public String checkHealth() {
        try {
            URL url = new URL(BASE_URL + "/health");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("GET");
            conn.setConnectTimeout(10000);
            conn.setReadTimeout(10000);

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream())
            );

            StringBuilder response = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            reader.close();
            return response.toString();

        } catch (Exception e) {
            System.out.println("Health Error: " + e.getMessage());
            return null;
        }
    }

    //  Generate API (POST)
    public String generateText(String input) {
        try {
            URL url = new URL(BASE_URL + "/generate");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("POST");
            conn.setConnectTimeout(10000);
            conn.setReadTimeout(10000);

            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            // JSON body
            String jsonInput = "{\"input\":\"" + input + "\"}";

            OutputStream os = conn.getOutputStream();
            os.write(jsonInput.getBytes());
            os.flush();
            os.close();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream())
            );

            StringBuilder response = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            reader.close();
            return response.toString();

        } catch (Exception e) {
            System.out.println("Generate Error: " + e.getMessage());
            return null; //  required
        }
    }

    // MAIN METHOD (fixes your error)
    public static void main(String[] args) {

        AiServiceClient client = new AiServiceClient();

        String health = client.checkHealth();
        System.out.println("Health: " + health);

        String response = client.generateText("Hello from Java");
        System.out.println("Response: " + response);
    }
}