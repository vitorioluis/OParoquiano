package br.com.oparoquiano.app.MeusAdapter;

import android.app.Activity;
import android.support.v4.app.FragmentManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.nostra13.universalimageloader.core.ImageLoader;

import java.util.List;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.Util.Util;
import br.com.oparoquiano.app.actMain;
import br.com.oparoquiano.app.fragments.frag_exibe_agenda;

/**
 * Created by luis on 11/06/17.
 */

public class AdapterListaCategoria extends RecyclerView.Adapter {
    private final List<Agenda> agendas;
    private final Activity act;
    private FragmentManager fm = null;

    public AdapterListaCategoria(List<Agenda> agendas, Activity act) {
        this.agendas = agendas;
        this.act = act;
    }

    public Agenda getAgenda(int position) {
        return this.agendas.get(position);
    }


    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(this.act).inflate(R.layout.layout_view_categoria, parent, false);

        viewHolderCategoria holder = new viewHolderCategoria(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder viewHolder, final int position) {
        viewHolderCategoria holder = (viewHolderCategoria) viewHolder;

        final Util util = new Util();
        final ImageLoader mImageLoader = util.ImgLoader(this.act);
        String url_logo = Auxiliar.url_img + this.getAgenda(position).getTip_img();
        mImageLoader.displayImage(url_logo, holder.imageView);
        holder.nome_categoria.setText(this.getAgenda(position).getTip_name().toString());

        holder.linearLayout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                fm = ((actMain) act).getSupportFragmentManager();
                Auxiliar.pk_search_agenda_tip_nome = getAgenda(position).getTip_name();

                android.support.v4.app.FragmentTransaction fragmentTransaction = fm.beginTransaction();
                fragmentTransaction.addToBackStack(null);
                fragmentTransaction.replace(R.id.containerView, new frag_exibe_agenda()).commit();
            }
        });
    }

    @Override
    public long getItemId(int position) {
        return agendas.get(position).getAge_id();
    }

    @Override
    public int getItemCount() {
        return agendas.size();
    }

    public class viewHolderCategoria extends RecyclerView.ViewHolder {
        public ImageView imageView;
        public TextView nome_categoria;
        public LinearLayout linearLayout;

        public viewHolderCategoria(View itemView) {
            super(itemView);

            imageView = (ImageView) itemView.findViewById(R.id.img_logo);
            nome_categoria = (TextView) itemView.findViewById(R.id.txt_nome_categ);
            linearLayout = (LinearLayout) itemView.findViewById(R.id.LinearLayout);
        }

    }
}
