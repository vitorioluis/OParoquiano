package br.com.oparoquiano.app.fragments;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.actMain;


public class frag_sobre extends Fragment {

    TextView txt_email, txt_site, txt_versao;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.act_sobre, container, false);

        txt_email = (TextView) view.findViewById(R.id.txt_email);
        txt_site = (TextView) view.findViewById(R.id.txt_site);
        txt_versao = (TextView) view.findViewById(R.id.txt_versao);

        return view;

    }

    @Override
    public void onActivityCreated(Bundle saveInstanceStates) {
        super.onActivityCreated(saveInstanceStates);

        ((AppCompatActivity)getContext()).getSupportActionBar().setSubtitle(R.string.Sobre);

        txt_versao.setText(Auxiliar.versao_app);
        txt_email.setText(Auxiliar.email_contato);
        txt_site.setText(Auxiliar.site);

    }


}
