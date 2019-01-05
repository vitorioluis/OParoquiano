package br.com.oparoquiano.app.DataBase;

import br.com.oparoquiano.app.Dominio.Entidades.Agenda;
import br.com.oparoquiano.app.Dominio.Entidades.Config;
import br.com.oparoquiano.app.Dominio.Entidades.IntecoesMissa;
import br.com.oparoquiano.app.Dominio.Entidades.Paroquia;
import br.com.oparoquiano.app.Dominio.Entidades.Pontuacao;

/**
 * Created by luis.vitorio on 04/03/2016.
 */
public class ScriptSql {


    public static String getCreateParoquia() {

        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS " + Paroquia.nomeTabela + "( ");
        strBuilder.append("_id INTEGER, ");
        strBuilder.append("dio_name varchar(100), ");
        strBuilder.append("par_name varchar(100), ");
        strBuilder.append("par_site varchar(100), ");
        strBuilder.append("par_num varchar(100), ");
        strBuilder.append("par_endereco varchar(250), ");
        strBuilder.append("par_cep varchar(100), ");
        strBuilder.append("par_cidade varchar(100), ");
        strBuilder.append("par_propaganda varchar(10), ");
        strBuilder.append("par_fav boolean default false, ");
        strBuilder.append("par_logo varchar(255)); ");

        return strBuilder.toString();
    }


    public static String getCreateAgenda() {

        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS " + Agenda.nomeTabela + "(");
        strBuilder.append("_id INTEGER,");
        strBuilder.append("par_id INTEGER,");
        strBuilder.append("par_name varchar(100), ");
        strBuilder.append("tip_name nvarchar(100),");
        strBuilder.append("age_data_inicio nvarchar(100),");
        strBuilder.append("age_data_fim nvarchar(100),");
        strBuilder.append("age_hora_inicio nvarchar(50),");
        strBuilder.append("age_hora_fim nvarchar(50),");
        strBuilder.append("age_desc nvarchar(255),");
        strBuilder.append("age_local_evento nvarchar(255),");
        strBuilder.append("age_img_divulga nvarchar(255),");
        strBuilder.append("tip_img nvarchar(255)); ");

        return strBuilder.toString();
    }


    public static String getCreatePotuacao() {

        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS " + Pontuacao.nomeTabela + " ( ");
        strBuilder.append("_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ");
        strBuilder.append("pon_tabela varchar(100) NOT NULL, ");
        strBuilder.append("pon_id_tabela INTEGER NOT NULL, ");
        strBuilder.append("pon_pontos INTEGER default(0)); ");

        return strBuilder.toString();
    }


    public static String getCreateLogin() {
        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS tb_lgn_login ( ");
        strBuilder.append("_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ");
        strBuilder.append("lgn_email varchar(100) NOT NULL, ");
        strBuilder.append("lgn_senha varchar(30) NOT NULL, ");
        strBuilder.append("lgn_hash varchar(100) NOT NULL); ");

        return strBuilder.toString();
    }

    public static String getCreateConfig() {
        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS " + Config.nomeTabela + " ( ");
        strBuilder.append("_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ");
        strBuilder.append("cfg_desc varchar(100),");//variavel de configuração
        strBuilder.append("cfg_valor INTEGER default(0));");

        return strBuilder.toString();
    }


    public static String getCreateIntecao() {
        StringBuilder strBuilder = new StringBuilder();

        strBuilder.append("CREATE TABLE IF NOT EXISTS " + IntecoesMissa.nomeTabela + " ( ");
        strBuilder.append("_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ");
        strBuilder.append("nome varchar(50),");
        strBuilder.append("intecao varchar(255),");
        strBuilder.append("paroquia INTEGER );");

        return strBuilder.toString();
    }

}
