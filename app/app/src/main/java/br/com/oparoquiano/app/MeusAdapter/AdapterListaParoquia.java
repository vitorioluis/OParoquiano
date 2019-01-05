package br.com.oparoquiano.app.MeusAdapter;

import android.app.Activity;
import android.app.Dialog;
import android.database.sqlite.SQLiteDatabase;
import android.support.v4.app.FragmentManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.nostra13.universalimageloader.core.ImageLoader;

import java.util.List;

import br.com.oparoquiano.app.DataBase.DataBase;
import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;
import br.com.oparoquiano.app.R;
import br.com.oparoquiano.app.Util.Auxiliar;
import br.com.oparoquiano.app.Util.Util;
import br.com.oparoquiano.app.actMain;
import br.com.oparoquiano.app.fragments.frag_selecao_categorias;

/**
 * Created by luis on 11/06/17.
 */

public class AdapterListaParoquia extends RecyclerView.Adapter {

    private final List<Paroquia> paroquias;
    private FragmentManager fm = null;
    private Activity act;

    public AdapterListaParoquia(List<Paroquia> paroquias, Activity act) {
        this.paroquias = paroquias;
        this.act = act;
    }


    public Paroquia getParoquia(int position) {

        return this.paroquias.get(position);
    }


    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(this.act).inflate(R.layout.layout_view_paroquia, parent, false);

        viewHolderParoquia holder = new viewHolderParoquia(view);

        return holder;
    }

    @Override
    public void onBindViewHolder(final RecyclerView.ViewHolder viewHolder, final int position) {
        final viewHolderParoquia holder = (viewHolderParoquia) viewHolder;

        final Util util = new Util();
        final ImageLoader mImageLoader = util.ImgLoader(this.act);
        String url_logo = Auxiliar.url_img + this.getParoquia(position).getPar_logo();
        mImageLoader.displayImage(url_logo, holder.imageView);
        holder.txt_nome_paroquia.setText(this.getParoquia(position).getPar_nome());
        //holder.txt_nome_cidade.setText(this.getParoquia(position).getPar_cidade());
        holder.txt_nome_diocese.setText("Diocese " + this.getParoquia(position).getDio_name());


        holder.linearLayout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Auxiliar.pk_search_categ = Integer.parseInt(getParoquia(position).getPar_id());
                Auxiliar.pk_search_agenda_par_id = getParoquia(position).getPar_id();

                fm = ((actMain) act).getSupportFragmentManager();
                android.support.v4.app.FragmentTransaction fragmentTransaction = fm.beginTransaction();
                fragmentTransaction.addToBackStack(null);
                fragmentTransaction.replace(R.id.containerView, new frag_selecao_categorias()).commit();
            }
        });


        holder.linearLayout.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {

                final Dialog dialog = new Dialog(act);
                dialog.setContentView(R.layout.layout_view_popup_paroquia);

                TextView txt_1 = (TextView) dialog.findViewById(R.id.txt_desc_paroquia);
                TextView txt_2 = (TextView) dialog.findViewById(R.id.txt_desc_diocese);
//                TextView txt_3 = (TextView) dialog.findViewById(R.id.txt_desc_padroeiro);
                TextView txt_4 = (TextView) dialog.findViewById(R.id.txt_desc_cidade);
                TextView txt_5 = (TextView) dialog.findViewById(R.id.txt_desc_site);
                TextView txt_6 = (TextView) dialog.findViewById(R.id.txt_desc_end);

                txt_1.setText(getParoquia(position).getPar_nome());
                txt_2.setText(getParoquia(position).getDio_name());
//                txt_3.setText(getParoquia(position).getPar_padroeiro());
              //  txt_4.setText(getParoquia(position).getPar_cidade());
                txt_5.setText(getParoquia(position).getPar_site());
                txt_6.setText(getParoquia(position).getPar_endereco() + " " + getParoquia(position).getPar_num());
                dialog.show();

                return true;
            }
        });


        if (this.getParoquia(position).getPar_fav()) {
            holder.btn_favorito.setImageResource(R.drawable.favorite_on);
        } else {
            holder.btn_favorito.setImageResource(R.drawable.favorite_off);
        }


        holder.btn_favorito.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                holder.btn_favorito.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        Boolean teste = getParoquia(position).getPar_fav();
                        String toast = "A Paróquia " + getParoquia(position).getPar_nome();

                        if (teste) {
                            getParoquia(position).setPar_fav(false);
                            holder.btn_favorito.setImageResource(R.drawable.favorite_off);
                            toast = toast.concat(" NÃO é mais sua favorita.");
                        } else {
                            getParoquia(position).setPar_fav(true);
                            holder.btn_favorito.setImageResource(R.drawable.favorite_on);
                            toast = toast.concat(" agora é sua favorita.");
                        }
                        Toast.makeText(act, toast, Toast.LENGTH_LONG).show();

                        DataBase dataBase = new DataBase(act);
                        SQLiteDatabase conn = dataBase.getWritableDatabase();

                        String sql = "update " + Paroquia.nomeTabela;
                        sql = sql.concat(" set par_fav='" + getParoquia(position).getPar_fav());
                        sql = sql.concat("' where _id='" + getParoquia(position).getPar_id() + "';");
                        conn.execSQL(sql);
                        conn.close();
                    }
                });

            }
        });
    }

    @Override
    public int getItemCount() {
        return this.paroquias.size();
    }


    @Override
    public long getItemId(int position) {
        return Integer.parseInt(this.paroquias.get(position).getPar_id());
    }


    public class viewHolderParoquia extends RecyclerView.ViewHolder {
        public ImageView imageView;
        public TextView txt_nome_cidade;
        public TextView txt_nome_paroquia;
        public TextView txt_nome_diocese;
        public LinearLayout linearLayout;
        public ImageButton btn_favorito;

        public viewHolderParoquia(View itemView) {
            super(itemView);
            imageView = (ImageView) itemView.findViewById(R.id.img_logo);

            txt_nome_paroquia = (TextView) itemView.findViewById(R.id.txt_nome_paroquia);
            //txt_nome_cidade = (TextView) itemView.findViewById(R.id.txt_nome_cidade);
            txt_nome_diocese = (TextView) itemView.findViewById(R.id.txt_nome_diocese);

            linearLayout = (LinearLayout) itemView.findViewById(R.id.LinearLayout);
            btn_favorito = (ImageButton) itemView.findViewById(R.id.btn_img_fvt);
        }

    }
}