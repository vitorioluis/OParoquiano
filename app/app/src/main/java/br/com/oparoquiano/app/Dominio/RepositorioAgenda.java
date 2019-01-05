package br.com.oparoquiano.app.Dominio;

import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;

/**
 * Created by luis.vitorio on 13/03/2016.
 */
public class RepositorioAgenda {
    SQLiteDatabase conn = null;

    public RepositorioAgenda(SQLiteDatabase conn) {
        this.conn = conn;
    }

    public void inserirAgenda(Agenda agenda) {
        ContentValues values = new ContentValues();

        values.put("_id", agenda.getAge_id());
        values.put("par_id", agenda.getPar_id());
        values.put("par_name", agenda.getPar_name());
        values.put("tip_name", agenda.getTip_name());
        values.put("age_data_inicio", agenda.getAge_data_inicio());
        values.put("age_data_fim ", agenda.getAge_data_fim());
        values.put("age_hora_inicio ", agenda.getAge_hora_inicio());
        values.put("age_hora_fim", agenda.getAge_hora_fim());
        values.put("age_desc", agenda.getAge_desc());
        values.put("age_local_evento", agenda.getAge_local_evento());
        values.put("tip_img", agenda.getTip_img());
        values.put("age_img_divulga",agenda.getAge_img_divulga());

        this.conn.insert(Agenda.nomeTabela, null, values);

    }


}
