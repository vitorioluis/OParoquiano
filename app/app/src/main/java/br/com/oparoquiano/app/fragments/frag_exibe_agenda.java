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

import java.util.ArrayList;
import java.util.List;

import br.com.oparoquiano.app.DataBase.DataBase;
import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.MeusAdapter.AdapterAgenda;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;


public class frag_exibe_agenda extends Fragment {

    List<Agenda> lst_exibir_agenda = new ArrayList<>();
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

        this.preencheListViewAgenda();

        if (lst_exibir_agenda.size() > 0) {
            ((AppCompatActivity)getContext()).getSupportActionBar().setSubtitle(lst_exibir_agenda.get(0).getTip_name());
            LayoutManager layoutManager = new LinearLayoutManager(getActivity(), LinearLayoutManager.VERTICAL, false);
            recyclerView.setHasFixedSize(true);

            recyclerView.setLayoutManager(layoutManager);
            recyclerView.setAdapter(new AdapterAgenda(lst_exibir_agenda, getActivity()));

//            recyclerView.addItemDecoration(new DividerItemDecoration(getContext(), DividerItemDecoration.VERTICAL));
        }
    }


    public void preencheListViewAgenda() {
        lst_exibir_agenda.clear();
        //Cursor cursor = conn.query("tb_diocese", null, null, null, null, null, null);
        String sql = "select _id,age_data_inicio,age_data_fim,age_hora_inicio,age_hora_fim,";
        sql = sql.concat("age_desc,age_local_evento,tip_name, age_img_divulga from ");
        sql = sql.concat(Agenda.nomeTabela);
        sql = sql.concat(" where tip_name ='" + Auxiliar.pk_search_agenda_tip_nome);
        sql = sql.concat("' and par_id =" + Auxiliar.pk_search_agenda_par_id);
        sql = sql.concat(" order by age_data_inicio, age_hora_inicio;");

        Cursor cursor = this.conn.rawQuery(sql, null);

        if (cursor.getCount() > 0) {
            cursor.moveToFirst();
            do {
                Agenda agenda = new Agenda();

                agenda.setAge_id(Integer.parseInt(cursor.getString(0)));
                agenda.setAge_data_inicio(cursor.getString(1));
                agenda.setAge_data_fim(cursor.getString(2));
                agenda.setAge_hora_inicio(cursor.getString(3));
                agenda.setAge_hora_fim(cursor.getString(4));
                agenda.setAge_desc(cursor.getString(5));
                agenda.setAge_local_evento(cursor.getString(6));
                agenda.setTip_name(cursor.getString(7));
                agenda.setAge_img_divulga(cursor.getString(8));

                lst_exibir_agenda.add(agenda);

            } while (cursor.moveToNext());
        }
        cursor.close();
    }


}
