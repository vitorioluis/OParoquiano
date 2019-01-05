package br.com.oparoquiano.app.fragments;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import br.com.oparoquiano.app.R;


public class frag_intencoes_missa extends Fragment {

    EditText edt_nome, edt_intencao;
    Spinner spd_paroquia;
    Button btn_enviar;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.act_intencoes_missas, container, false);

        edt_nome = (EditText) view.findViewById(R.id.edt_nome);
        spd_paroquia = (Spinner) view.findViewById(R.id.spn_paroquia);
        edt_intencao = (EditText) view.findViewById(R.id.edt_intencao);
        btn_enviar = (Button)view.findViewById(R.id.btn_enviar);


        return view;

    }

    @Override
    public void onActivityCreated(Bundle saveInstanceStates) {
        super.onActivityCreated(saveInstanceStates);

        ((AppCompatActivity) getContext()).getSupportActionBar().setSubtitle(R.string.Sobre);

    }




}
