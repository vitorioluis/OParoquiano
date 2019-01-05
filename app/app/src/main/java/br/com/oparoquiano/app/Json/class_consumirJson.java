package br.com.oparoquiano.app.Json;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import br.com.oparoquiano.app.Util.Auxiliar;

/**
 * Created by luis.vitorio on 07/04/2016.
 */
public class class_consumirJson {


    public static String makeRequest(String pagina) {
        String urlAddress = Auxiliar.url_api;
        urlAddress = urlAddress.concat(pagina);
        urlAddress = urlAddress.concat("/");

        HttpURLConnection con = null;
        URL url = null;
        String response = null;
        try {
            url = new URL(urlAddress);

            con = (HttpURLConnection) url.openConnection();
            response = readStream(con.getInputStream());

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            con.disconnect();
        }
        return response;
    }


    private static String readStream(InputStream in) {
        BufferedReader reader = null;
        StringBuilder builder = new StringBuilder();
        try {
            reader = new BufferedReader(new InputStreamReader(in));
            String line = null;
            while ((line = reader.readLine()) != null) {
                builder.append(line + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return builder.toString();
    }

}
