package br.com.oparoquiano.app.Atualiza;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.Dominio.RepositorioAgenda;
import br.com.oparoquiano.app.Json.class_consumirJson;
import br.com.oparoquiano.app.Util.Auxiliar;


/**
 * Created by luis on 16/05/16.
 */
public class AtualizaAgenda {
    private RepositorioAgenda repositorioAgenda;
    private SQLiteDatabase conn;

    public AtualizaAgenda(SQLiteDatabase conn) {
        this.repositorioAgenda = new RepositorioAgenda(conn);
        this.conn = conn;
    }

    public void Executa(Context context, int pk) {
        Agenda agenda = new Agenda();
        String x = "agenda/" + Auxiliar.token + "/" + Integer.toString(pk);

        String response = class_consumirJson.makeRequest(x);
        if (response != null) {
            this.delete(pk);
            //Toast.makeText(context, "Carregando...", Toast.LENGTH_SHORT).show();
            try {
                JSONObject result = new JSONObject(response);
                JSONArray resultArray = result.getJSONArray(Auxiliar.json_raiz);
                for (int i = 0; i < resultArray.length(); i++) {

                    JSONObject json = resultArray.getJSONObject(i);

                    agenda.setAge_id(json.getInt("id"));

                    agenda.setPar_id(json.getInt("paroquia__id"));
                    agenda.setPar_name(json.getString("paroquia__par_name"));
                    agenda.setTip_name(json.getString("tipo__tipo_agendamento"));
                    agenda.setAge_data_inicio(json.getString("age_data_inicio"));
                    agenda.setAge_data_fim(json.getString("age_data_fim"));
                    agenda.setAge_hora_inicio(json.getString("age_hora_inicio"));
                    agenda.setAge_hora_fim(json.getString("age_hora_fim"));
                    agenda.setAge_desc(json.getString("age_desc"));
                    agenda.setAge_local_evento(json.getString("age_local_evento"));
                    agenda.setTip_img(json.getString("tipo__tipo_img"));
                    agenda.setAge_img_divulga(json.getString("age_img"));

                    repositorioAgenda.inserirAgenda(agenda);
                }


            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }

    private void delete(int id) {
        this.conn.execSQL("delete from " + Agenda.nomeTabela + " where par_id='" + Integer
                .toString(id) + "';");
    }
}
