import pandas as pd

def filtrarDados():

    print("iniciando...")

    df = pd.read_csv(
        "microdados_ed_basica_2024.csv", sep=";", encoding="latin1", low_memory=False
    )

    mapa_colunas = {
        "NO_ENTIDADE": "no_entidade",
        "CO_ENTIDADE": "co_entidade",
        "NO_UF": "no_uf",
        "SG_UF": "sg_uf",
        "CO_UF": "co_uf",
        "NO_MUNICIPIO": "no_municipio",
        "CO_MUNICIPIO": "co_municipio",
        "NO_MESORREGIAO": "no_mesorregiao",
        "CO_MESORREGIAO": "co_mesorregiao",
        "NO_MICRORREGIAO": "no_microrregiao",
        "CO_MICRORREGIAO": "co_microrregiao",
        "NU_ANO_CENSO": "nu_ano_censo",
        "NO_REGIAO": "no_regiao",
        "CO_REGIAO": "co_regiao",
        "QT_MAT_BAS": "qt_mat_bas",
        "QT_MAT_INF": "qt_mat_inf",
        "QT_MAT_FUND": "qt_mat_fund",
        "QT_MAT_MED": "qt_mat_med",
        "QT_MAT_PROF": "qt_mat_prof",
        "QT_MAT_EJA": "qt_mat_eja",
        "QT_MAT_ESP": "qt_mat_esp"
    }

    colunas_existentes = [col for col in mapa_colunas.keys() if col in df.columns]

    df_pb = df[df["SG_UF"] == "PB"]

    df_pb = df_pb[colunas_existentes]

    df_pb = df_pb.rename(columns=mapa_colunas)

    return df_pb


def salvarJson(df):
    print("...")
    df.to_json("instituicoes_paraiba.json", orient="records", force_ascii=False, indent=4
    )
    print("arquiso instituicoes_paraiba.json gerado com sucesso")

df_pb = filtrarDados()
salvarJson(df_pb)