
import java.io.*;
import java.net.*;
import java.util.*;

public class Server {

    public static void main(String[] args) {
        try
        {
            System.out.println("Starting the Server!");
            ServerSocket s = new ServerSocket(8080);
            //This creates a new socket at port 8080.
            Socket sock=s.accept();
            DataInputStream din = new DataInputStream(sock.getInputStream());
            DataOutputStream dout = new DataOutputStream(sock.getOutputStream());
            Scanner sc = new Scanner(System.in);
            String mesgreceive="", mesgsent="";

            do {

                mesgreceive = din.readUTF();
                System.out.println("Client Message:" + mesgreceive);
                System.out.println("Please enter your message");
                mesgsent = sc.nextLine();
                dout.writeUTF(mesgsent);
                dout.flush();


            } while (!mesgsent.equals("kill") && !mesgreceive.equals("kill"));
            din.close();
            dout.close();

            System.out.println("Closing the connection socket!");
            s.close();
        }
        catch(Exception e)
        {
            System.out.println("There was an error in the program! " + e.getMessage());
        }
    }
}