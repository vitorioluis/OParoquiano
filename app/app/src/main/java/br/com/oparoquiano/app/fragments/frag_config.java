package br.com.oparoquiano.app.fragments;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;

import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;


public class frag_config extends Fragment {

    CheckBox ckb_notificacao;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.act_config, container, false);
        ckb_notificacao = (CheckBox) view.findViewById(R.id.ckb_notificacao);

        return view;

    }

    @Override
    public void onActivityCreated(Bundle saveInstanceStates) {
        super.onActivityCreated(saveInstanceStates);

        ((AppCompatActivity)getContext()).getSupportActionBar().setSubtitle(R.string.config);

        if (Auxiliar.receber_notificacao_valor == 1) {
            ckb_notificacao.setChecked(true);
        } else {
            ckb_notificacao.setChecked(false);
        }

    }


}
