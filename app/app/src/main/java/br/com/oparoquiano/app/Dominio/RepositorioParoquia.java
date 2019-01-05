package br.com.oparoquiano.app.Dominio;


import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;

import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;

/**
 * Created by luis.vitorio on 07/03/2016.
 */
public class RepositorioParoquia {
    private final SQLiteDatabase conn;


    public RepositorioParoquia(SQLiteDatabase conn) {
        this.conn = conn;
    }

    public void insertIgreja(Paroquia paroquia) {
        ContentValues values = new ContentValues();

        values.put("_id", paroquia.getPar_id());
        values.put("dio_name", paroquia.getDio_name());
        values.put("par_name", paroquia.getPar_nome());
        values.put("par_site", paroquia.getPar_site());
        values.put("par_cep", paroquia.getPar_cep());
        values.put("par_endereco", paroquia.getPar_endereco());
        values.put("par_cidade", paroquia.getPar_cidade());
        values.put("par_propaganda", paroquia.getPar_propaganda());
        values.put("par_logo", paroquia.getPar_logo());

        this.conn.insert(Paroquia.nomeTabela, null, values);

    }


}