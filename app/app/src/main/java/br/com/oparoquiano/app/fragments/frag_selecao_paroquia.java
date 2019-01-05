package br.com.oparoquiano.app.fragments;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.RecyclerView.LayoutManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import br.com.oparoquiano.app.Atualiza.AtualizaParoquia;
import br.com.oparoquiano.app.DataBase.DataBase;
import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;
import br.com.oparoquiano.app.MeusAdapter.AdapterListaParoquia;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Util;


public class frag_selecao_paroquia extends Fragment {

    List<Paroquia> lstParoquia = new ArrayList<>();
    RecyclerView recyclerView;
    private SQLiteDatabase conn;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.act_recycler_view, container, false);
        setHasOptionsMenu(true);

        DataBase dataBase = new DataBase(getContext());
        this.conn = dataBase.getWritableDatabase();

        recyclerView = (RecyclerView) view.findViewById(R.id.recycler);

        // StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        // StrictMode.setThreadPolicy(policy);
        // VerificaPorAtualizacaoParoquia();

        return view;
    }

    @Override
    public void onActivityCreated(Bundle saveInstanceStates) {
        super.onActivityCreated(saveInstanceStates);
        ((AppCompatActivity)getContext()).getSupportActionBar().setSubtitle(R.string.selecao_de_paroquia);

        this.preencheListViewParoquia();

        if (lstParoquia.size() > 0) {
            LayoutManager layoutManager = new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL, false);
            recyclerView.setHasFixedSize(true);

            recyclerView.setLayoutManager(layoutManager);
            recyclerView.setAdapter(new AdapterListaParoquia(lstParoquia, getActivity()));

//            recyclerView.addItemDecoration(new DividerItemDecoration(getContext(), DividerItemDecoration.VERTICAL));
        }
    }


    public void VerificaPorAtualizacaoParoquia() {
        if (Util.testaConexao(getContext())) {
            AtualizaParoquia atualizaParoquia = new AtualizaParoquia(this.conn);
            atualizaParoquia.Executa(getContext());
        } else {
            Toast.makeText(getContext(), "Internet Indisponivel.", Toast.LENGTH_SHORT).show();
        }
    }

    public void preencheListViewParoquia() {
        lstParoquia.clear();
        //Cursor cursor = conn.query("tb_diocese", null, null, null, null, null, null);
        String sql = "select _id,par_name,par_cidade,par_logo,dio_name,par_fav,par_cidade, par_site from ";
        sql = sql.concat(Paroquia.nomeTabela);
        sql = sql.concat(" order by par_fav desc, dio_name,par_name;");

        Cursor cursor = this.conn.rawQuery(sql, null);

        if (cursor.getCount() > 0) {
            cursor.moveToFirst();
            do {
                Paroquia paroquia = new Paroquia();

                paroquia.setPar_id(cursor.getString(0));
                paroquia.setPar_nome(cursor.getString(1));
                paroquia.setPar_cidade(cursor.getString(2));
                paroquia.setPar_logo(cursor.getString(3));
                paroquia.setDio_name(cursor.getString(4));
                paroquia.setPar_fav(Boolean.parseBoolean(cursor.getString(5)));
                paroquia.setPar_cidade(cursor.getString(6));
                paroquia.setPar_site(cursor.getString(7));

                lstParoquia.add(paroquia);

            } while (cursor.moveToNext());
        }
        cursor.close();
    }


}
