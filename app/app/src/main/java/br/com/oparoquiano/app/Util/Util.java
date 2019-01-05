package br.com.oparoquiano.app.Util;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

import com.nostra13.universalimageloader.core.DisplayImageOptions;
import com.nostra13.universalimageloader.core.ImageLoader;
import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;
import com.nostra13.universalimageloader.core.display.FadeInBitmapDisplayer;

import java.text.SimpleDateFormat;
import java.util.Date;

import br.com.oparoquiano.app.R;

/**
 * Created by luis.vitorio on 14/04/2016.
 */
public class Util {

    public static boolean testaConexao(Context context) {
        ConnectivityManager cm = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo netInfo = cm.getActiveNetworkInfo();
        Boolean teste = false;

        if (netInfo != null && netInfo.isConnected())
            teste = true;

        return teste;
    }

    public static String geraDataNow() {
        String f = "dd/MM/yyyy";

        SimpleDateFormat sdf = new SimpleDateFormat(f);
        Date date = new Date();
        return sdf.format(date).toString();
    }


    public static Boolean autorizar_atualizacao(String nome_par) {
        Boolean retorno = null;
        long tempo_corrente = System.currentTimeMillis();
        long calc;

        if (Auxiliar.dic_ultima_atualizacao.containsKey(nome_par)) {
            long tempo = Auxiliar.dic_ultima_atualizacao.get(nome_par);

            if (tempo_corrente > tempo) {
                calc = tempo_corrente + Auxiliar.tempo_minimo_para_atualizacao;
                Auxiliar.dic_ultima_atualizacao.put(nome_par, calc);
                retorno = true;
            }

        } else {
            calc = tempo_corrente - Auxiliar.tempo_minimo_para_atualizacao;
            Auxiliar.dic_ultima_atualizacao.put(nome_par, calc);
            retorno = true;
        }

        if (retorno == null) {
            retorno = false;
        }

        return retorno;
    }

    public String formato_data(String data_in, String formato) {
        String data_out = "";
        String[] data_split;

        if ((formato == "ddmmaaaa") & (data_in.length() > 2)) {
            data_split = data_in.split("-");
            data_out = data_split[2];
            data_out = data_out.concat("-");
            data_out = data_out.concat(data_split[1]);
            data_out = data_out.concat("-");
            data_out = data_out.concat(data_split[0]);
        }
        return data_out;
    }

    public ImageLoader ImgLoader(Context context) {
        ImageLoader mImageLoader;
        DisplayImageOptions mDisplayImageOptions = new DisplayImageOptions.Builder()
                .showImageForEmptyUri(R.drawable.about)
                .showImageOnFail(R.drawable.fail)
                .showImageOnLoading(R.drawable.loading)
                .cacheInMemory(true)
                .cacheOnDisk(true)
                .displayer(new FadeInBitmapDisplayer(1000))
                .build();

        ImageLoaderConfiguration conf = new ImageLoaderConfiguration.Builder(context)
                .defaultDisplayImageOptions(mDisplayImageOptions)
                .memoryCacheSize(50 * 1024 * 1024)
                .diskCacheSize(50 * 1024 * 1024)
                .threadPoolSize(5)
                .writeDebugLogs()
                .build();
        mImageLoader = ImageLoader.getInstance();
        mImageLoader.init(conf);

//        PauseOnScrollListener mPauseOnScrollListener = new PauseOnScrollListener(mImageLoader, true, true);

//        lvPosts = (ListView) findViewById(R.id.lvPosts);
//        lvPosts.setAdapter(new AdapterListView(MainActivity.this, list, mImageLoader));
//        lvPosts.setOnScrollListener(mPauseOnScrollListener);
        return mImageLoader;
    }


}


//    public static Boolean autorizar_atualizacao() {
//        Boolean retorno;
//        long tempo_corrente = System.currentTimeMillis();
//
//        if (Auxiliar.ultima_atualizacao == 0) {
//            retorno = true;
//            Auxiliar.ultima_atualizacao = tempo_corrente - Auxiliar.tempo_minimo_para_atualizacao;
//        } else if (tempo_corrente >= Auxiliar.ultima_atualizacao) {
//            retorno = true;
//            Auxiliar.ultima_atualizacao = tempo_corrente + Auxiliar.tempo_minimo_para_atualizacao;
//        } else {
//            retorno = false;
//        }
//
//        return retorno;
//    }