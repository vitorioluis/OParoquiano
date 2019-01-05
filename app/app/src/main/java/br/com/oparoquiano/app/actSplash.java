package br.com.oparoquiano.app;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.os.Handler;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.widget.Toast;

import java.util.HashMap;

import br.com.oparoquiano.app.Atualiza.AtualizaParoquia;
import br.com.oparoquiano.app.DataBase.DataBase;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.Util.Util;

/**
 * Created by luis on 19/06/17.
 */

public class actSplash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_splash);

        Handler handle = new Handler();
        handle.postDelayed(new Runnable() {
            @Override
            public void run() {
                primeira_atualizacao();
                mostrarMain();
            }
        }, 1000);
    }

    private void mostrarMain() {
        Intent intent = new Intent(actSplash.this, actMain.class);
        startActivity(intent);
        finish();
    }

    private void primeira_atualizacao() {
        String completa_url = "";
        DataBase dataBase = new DataBase(actSplash.this);
        SQLiteDatabase conn = dataBase.getWritableDatabase();

        Auxiliar.dic_ultima_atualizacao = new HashMap<>();

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        if (Util.testaConexao(actSplash.this) == true) {
            AtualizaParoquia atualizaParoquia = new AtualizaParoquia(conn);
            atualizaParoquia.Executa(actSplash.this, completa_url);
        } else {
            Toast.makeText(actSplash.this, "Internet Indisponivel.", Toast.LENGTH_LONG).show();
        }

    }

}
