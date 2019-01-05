package br.com.oparoquiano.app.fragments;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.os.StrictMode;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import br.com.oparoquiano.app.Atualiza.AtualizaAgenda;
import br.com.oparoquiano.app.DataBase.DataBase;
import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.MeusAdapter.AdapterListaCategoria;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.Util.Util;

//import android.support.v7.widget.DividerItemDecoration;


public class frag_selecao_categorias extends Fragment {

    List<Agenda> lstAgenda = new ArrayList<>();
    RecyclerView recyclerView;
    private SQLiteDatabase conn;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.act_recycler_view, container, false);

        DataBase dataBase = new DataBase(getContext());
        this.conn = dataBase.getWritableDatabase();
        recyclerView = (RecyclerView) view.findViewById(R.id.recycler);

        return view;
    }

    @Override
    public void onActivityCreated(Bundle saveInstanceStates) {
        super.onActivityCreated(saveInstanceStates);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        if (Util.autorizar_atualizacao(Auxiliar.pk_search_agenda_par_id) == true) {
            VerificaPorAtualizacaoAgenda(Auxiliar.pk_search_categ);
        }

        this.preencheListViewAgenda();

        if (lstAgenda.size() > 0) {
            ((AppCompatActivity)getContext()).getSupportActionBar().setSubtitle(lstAgenda.get(0).getPar_name());
            RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL, false);
            recyclerView.setHasFixedSize(true);

            recyclerView.setLayoutManager(layoutManager);
            recyclerView.setAdapter(new AdapterListaCategoria(lstAgenda, getActivity()));

//            recyclerView.addItemDecoration(new DividerItemDecoration(getContext(), DividerItemDecoration.VERTICAL));
        }
    }

    public void VerificaPorAtualizacaoAgenda(int pk) {

        if (Util.testaConexao(getContext())) {
            AtualizaAgenda atualizaAgenda = new AtualizaAgenda(this.conn);
            atualizaAgenda.Executa(getContext(), pk);
        } else {
            Toast.makeText(getContext(), "Internet Indisponivel.", Toast.LENGTH_SHORT).show();
        }

    }

    public void preencheListViewAgenda() {
        lstAgenda.clear();
        //Cursor cursor = conn.query("tb_diocese", null, null, null, null, null, null);
        String sql = "select _id,tip_name,tip_img,par_name,par_id from ";
        sql = sql.concat(Agenda.nomeTabela);
        sql = sql.concat(" where par_id=" + Auxiliar.pk_search_agenda_par_id);
        sql = sql.concat(" group by tip_name");
        sql = sql.concat(" order by tip_name;");

        Cursor cursor = this.conn.rawQuery(sql, null);

        if (cursor.getCount() > 0) {
            cursor.moveToFirst();
            do {
                Agenda agenda = new Agenda();
                agenda.setAge_id(cursor.getInt(0));
                agenda.setTip_name(cursor.getString(1));
                agenda.setTip_img(cursor.getString(2));
                agenda.setPar_name(cursor.getString(3));
                agenda.setPar_id(cursor.getInt(4));

                lstAgenda.add(agenda);

            } while (cursor.moveToNext());
        }
        cursor.close();

    }


}
