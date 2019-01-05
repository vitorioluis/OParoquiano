package br.com.oparoquiano.app.Atualiza;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;
import br.com.oparoquiano.app.Dominio.RepositorioParoquia;
import br.com.oparoquiano.app.Json.class_consumirJson;
import br.com.oparoquiano.app.Util.Auxiliar;


/**
 * Created by luis on 16/05/16.
 */
public class AtualizaParoquia {
    private RepositorioParoquia repositorioParoquia;
    private SQLiteDatabase conn;


    public AtualizaParoquia(SQLiteDatabase conn) {
        this.repositorioParoquia = new RepositorioParoquia(conn);
        this.conn=conn;
    }

    public void Executa(Context context) {
        this.Executa(context, "");
    }


    public void Executa(Context context, String primeira) {
        Paroquia paroquia = new Paroquia();
        String url = "paroquia/" + Auxiliar.token + "/" + primeira;

        String response = class_consumirJson.makeRequest(url);
        if (response != null) {
            //Toast.makeText(context, "Atualizando...", Toast.LENGTH_SHORT).show();
            this.delete_paroquias();
            try {
                JSONObject result = new JSONObject(response);
                JSONArray resultArray = result.getJSONArray(Auxiliar.json_raiz);
                for (int i = 0; i < resultArray.length(); i++) {

                    JSONObject json = resultArray.getJSONObject(i);

                    paroquia.setPar_id(json.getString("id"));

                    paroquia.setDio_name(json.getString("diocese__dio_name"));
                    paroquia.setPar_site(json.getString("par_site"));
                    paroquia.setPar_logo(json.getString("par_logo"));
                    paroquia.setPar_cep(json.getString("par_cep"));
                    paroquia.setPar_nome(json.getString("par_name"));
                    paroquia.setPar_num(json.getString("par_num"));
                    paroquia.setPar_cidade(json.getString("par_cidade"));
                    paroquia.setPar_endereco(json.getString("par_endereco"));
                    paroquia.setPar_propaganda(json.getString("par_propaganda"));
                    paroquia.setPar_fav(false);



                    repositorioParoquia.insertIgreja(paroquia);

                }


            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

    }

    private void delete_paroquias(){
        String sql = "delete from "+ Paroquia.nomeTabela +";";
        //this.conn.execSQL("delete from "+ Paroquia.nomeTabela+" where _id='"+ id +"';");
        this.conn.execSQL(sql);
    }


}
