import java.util.Scanner;

public class MessageEncryptionApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Generate a DES key (should be securely stored and shared)
            MessageEncryption.generateDESKey();

            boolean running = true;
            while (running) {
                // User's message
                System.out.print("\nEnter your message (type 'exit' to quit): ");
                String message = scanner.nextLine();

                if ("exit".equalsIgnoreCase(message.trim())) {
                    running = false; // Exit the loop
                } else {
                    System.out.println("Original Message: " + message);

                    // Encrypt the message
                    String encrypted = MessageEncryption.encryptMessage(message);
                    System.out.println("Encrypted Message: " + encrypted);

                    // Decrypt the message
                    String decrypted = MessageEncryption.decryptMessage(encrypted);
                    System.out.println("Decrypted Message: " + decrypted);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}
