package br.com.oparoquiano.app.MeusAdapter;

import android.app.Activity;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ExpandableListView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.nostra13.universalimageloader.core.ImageLoader;

import java.util.List;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.Util.Util;

/**
 * Created by luis on 11/06/17.
 */

public class AdapterAgenda extends RecyclerView.Adapter {
    private final List<Agenda> agendas;
    private final Activity act;

    public AdapterAgenda(List<Agenda> agendas, Activity act) {
        this.agendas = agendas;
        this.act = act;
    }

    public Agenda getAgenda(int position) {
        return this.agendas.get(position);
    }


    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(this.act).inflate(R.layout.layout_view_agenda, parent, false);

        viewHolderAgenda holder = new viewHolderAgenda(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder viewHolder, final int position) {
        viewHolderAgenda holder = (viewHolderAgenda) viewHolder;

        String data = this.getAgenda(position).getAge_data_inicio();
        String hora = this.getAgenda(position).getAge_hora_inicio();
        if (hora.equals("None")) {
            hora = "-";
        }

        holder.txt_local.setText(this.getAgenda(position).getAge_local_evento());
        holder.txt_data.setText(data);
        holder.txt_hora.setText(hora);
        holder.txt_desc.setText(this.getAgenda(position).getAge_desc().toString());

        if (this.getAgenda(position).getAge_img_divulga() != null) {
            Util util = new Util();
            final ImageLoader mImageLoader = util.ImgLoader(this.act);
            String url_logo = Auxiliar.url_img + this.getAgenda(position).getAge_img_divulga();
            mImageLoader.displayImage(url_logo, holder.iv);
        }

    }

    @Override
    public long getItemId(int position) {
        return agendas.get(position).getAge_id();
    }

    @Override
    public int getItemCount() {
        return agendas.size();
    }

    public class viewHolderAgenda extends RecyclerView.ViewHolder {
        public TextView txt_local, txt_data, txt_hora, txt_desc;
        public LinearLayout linearLayout;
        public ImageView iv;
        public ExpandableListView expandableListView;

        public viewHolderAgenda(View itemView) {
            super(itemView);

//            txt_tipo = (TextView) itemView.findViewById(R.id.txt_tipo);
            txt_local = (TextView) itemView.findViewById(R.id.txt_local);
            txt_data = (TextView) itemView.findViewById(R.id.txt_data);
            txt_hora = (TextView) itemView.findViewById(R.id.txt_hora);
            txt_desc = (TextView) itemView.findViewById(R.id.txt_desc);
            iv = (ImageView) itemView.findViewById(R.id.img_divulgacao);
//            expandableListView = (ExpandableListView)itemView.findViewById(R.id.expand_text_view);

            linearLayout = (LinearLayout) itemView.findViewById(R.id.LinearLayout_1);
        }

    }
}
