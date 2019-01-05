package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis.vitorio on 13/03/2016.
 */
public class Agenda {
    public static String nomeTabela = "tb_agenda";


    private int age_id;
    private int par_id;
    private String par_name;
    private String tip_name;
    private String age_data_inicio;
    private String age_data_fim;
    private String age_hora_inicio;
    private String age_hora_fim;
    private String age_desc;
    private String age_local_evento;
    private String tip_img;
    private String age_img_divulga;


    public String getPar_id() {
        return Integer.toString(par_id);
    }

    public void setPar_id(int par_id) {
        this.par_id = par_id;
    }

    public String getAge_data_inicio() {
        return age_data_inicio;
    }

    public void setAge_data_inicio(String age_data_inicio) {
        this.age_data_inicio = age_data_inicio;
    }

    public String getAge_data_fim() {
        return age_data_fim;
    }

    public void setAge_data_fim(String age_data_fim) {
        this.age_data_fim = age_data_fim;
    }

    public String getAge_hora_inicio() {
        return age_hora_inicio;
    }

    public void setAge_hora_inicio(String age_hora_inicio) {
        this.age_hora_inicio = age_hora_inicio;
    }

    public String getAge_hora_fim() {
        return age_hora_fim;
    }

    public void setAge_hora_fim(String age_hora_fim) {
        this.age_hora_fim = age_hora_fim;
    }

    public String getAge_desc() {
        return age_desc;
    }

    public void setAge_desc(String age_desc) {
        this.age_desc = age_desc;
    }

    public String getAge_local_evento() {
        return age_local_evento;
    }

    public void setAge_local_evento(String age_local_evento) {
        this.age_local_evento = age_local_evento;
    }

    public Integer getAge_id() {
        return age_id;
    }

    public void setAge_id(Integer age_id) {
        this.age_id = age_id;
    }

    public String getTip_name() {
        return tip_name;
    }

    public void setTip_name(String tip_name) {
        this.tip_name = tip_name;
    }

    public String getTip_img() {
        return tip_img;
    }

    public void setTip_img(String tip_img) {
        this.tip_img = tip_img;
    }

    public String getPar_name() {
        return par_name;
    }

    public void setPar_name(String par_name) {
        this.par_name = par_name;
    }

    public String getAge_img_divulga() {
        return age_img_divulga;
    }

    public void setAge_img_divulga(String age_img_divulga) {
        this.age_img_divulga = age_img_divulga;
    }
}
