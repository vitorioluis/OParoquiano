package br.com.oparoquiano.app.DataBase;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;

/**
 * Created by luis.vitorio on 04/03/2016.
 */


public class DataBase extends SQLiteOpenHelper {
    public static final String banco = "db.paroquiano";
    SQLiteDatabase db;


    public DataBase(Context context) {

        super(context, banco, null, 36);//1 = versão
        db = this.getWritableDatabase();
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(ScriptSql.getCreateParoquia());
        db.execSQL(ScriptSql.getCreateAgenda());
        db.execSQL(ScriptSql.getCreateIntecao());
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {

        db.execSQL("DROP TABLE IF EXISTS " + Paroquia.nomeTabela + ";");
        db.execSQL("DROP TABLE IF EXISTS " + Agenda.nomeTabela + ";");
        onCreate(db);

    }

    public void delete(){

    }

}
