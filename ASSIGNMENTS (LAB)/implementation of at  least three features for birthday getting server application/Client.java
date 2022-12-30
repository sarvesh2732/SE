
import java.net.*;
import java.io.*;
import java.util.*;


public class Client
{


    public static void main(String[] args) {
        try {
            //At first we create a socket
            Socket clientsock=new Socket("localhost",8080);
            DataOutputStream out = new DataOutputStream(clientsock.getOutputStream());
            DataInputStream in =new DataInputStream(clientsock.getInputStream());
            String receivemsg="",sendmesg="";
            Scanner sc = new Scanner(System.in);

            out.writeUTF("Happy Birthday Server!");
            out.flush();
            while(true)
            {
                //For this case, we will be sending a message from the client to the server first.
                //We don’t want to be stuck with a deadlock now.
                receivemsg=in.readUTF();
                System.out.println("Server Says: "+receivemsg);
                System.out.println("Please enter your message");
                sendmesg=sc.nextLine();

                out.writeUTF(sendmesg);
                out.flush();
                if(receivemsg.equals("kill")||sendmesg.equals("kill"))
                {
                    System.out.println("Someone broke the conversation!");
                    break;
                }


            }
            sc.close();
            out.close();
            in.close();

            clientsock.close();


        } catch (Exception e) {
            //TODO: handle exception
            System.out.println("There is an error in the system!");
            System.out.println(e.getMessage());

        }
    }
}