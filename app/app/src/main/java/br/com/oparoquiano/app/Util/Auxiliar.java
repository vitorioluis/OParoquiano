package br.com.oparoquiano.app.Util;

import java.util.Map;

/**
 * Created by luis on 16/06/17.
 */

public class Auxiliar {
    public static String versao_app = "Versão: 1.13";
    public static String site = "www.oparoquiano.com.br";
    public static String email_contato = "contato@oparoquiano.com.br";

    public static String url_raiz = "http://app.oparoquiano.com.br/";
    public static String url_img = url_raiz + "media/";
    public static String url_api = url_raiz + "api/json_";

    public static Integer pk_search_categ;
    public static String pk_search_agenda_tip_nome = null;
    public static String pk_search_agenda_par_id;

    public static long tempo_minimo_para_atualizacao = 300000;// 1 minuto = 60000
    public static Map<String, Long> dic_ultima_atualizacao;

    //configurações
    public static int receber_notificacao_valor = 1;
    public static String receber_noticacao_texto = "notificacao";
    public static String json_raiz = "fields";

    public static String link_google_play = "https://play.google.com/store/apps/details?id=br.com.oparoquiano.app";
    public static String token = "92ad3305eadff39c271384f3912c704dbd053734974e5e0e14dbdfca6586d153cafb6aee6217443800b3aa872be4da07";
}
