<template>
    <div class="bg-neutral h-c100">
        <!-- Main content -->
        <div class="main-content">
            <!-- Header -->
            <div class="header bg-default py-7 py-lg-8 pt-lg-9">
                <div class="separator separator-bottom separator-skew zindex-100">
                    <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
                        xmlns="http://www.w3.org/2000/svg">
                        <polygon class="fill-neutral" points="2560 0 2560 300 0 100"></polygon>
                    </svg>
                </div>
            </div>
            <!-- Page content -->
            <div class="container mt--8 pb-8">
                <div class="row justify-content-center">
                    <div class="col-lg-12 col-md-7">
                        <div class="card bg-white mb-0 no-shaddow">

                            <div class="card-body px-lg-4 py-lg-4">
                                <form role="form" v-on:keyup.enter="login">
                                    <h3>Cadastro de alunos</h3>
                                    <div class="form-group mb-3 mt-3" style="width:22rem; float: left;">
                                        <div class="input-group input-group-merge input-group-alternative">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text"><i class="ni ni-email-83"></i></span>
                                            </div>
                                            <input class="form-control" placeholder="Nome" type="text" v-model="nome">
                                        </div>
                                    </div>
                                    <div class="form-group mb-3 mt-3" style="width:22rem;float: left;margin-left: 1rem;">
                                        <div class="input-group input-group-merge input-group-alternative">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text"><i class="ni ni-email-83"></i></span>
                                            </div>
                                            <input class="form-control" placeholder="E-mail" type="email" v-model="nome">
                                        </div>
                                    </div>
                                    <div class="form-group mb-3 mt-3" style="width:20rem;float: left;margin-left: 1rem;">
                                        <div class="input-group input-group-merge input-group-alternative">
                                            <div class="input-group-prepend">
                                                <span class="input-group-text"><i class="ni ni-email-83"></i></span>
                                            </div>
                                            <input class="form-control" placeholder="Curso" type="text" v-model="curso">
                                        </div>
                                    </div>
                                    <div class="text-center">
                                        <button type="button" class="btn btn-warning"
                                            @click="cadastrar(
                                              data['Nome'],
                                              data['Email'],
                                              data['Curso'],
                                            )">Cadastrar</button>
                                    </div>
                                   
                                </form>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<!-- <script>
import store from "@/store/store";
import axios from "axios";
import helper from "@/helper";

export default {
  name: "Cadastro",
  created() {

    // Puxa Empresas
    axios
      .get(`${process.env.VUE_APP_API}/Fechamento/allEmpresas`, {
        headers: {
          Authorization: `Bearer ${this.state.user.token}`,
        },
      })
      .then((resp) => {
        this.empresasData = resp.data;
      })
      .catch(() => {
        // nada
      });

  },

  //RETORNA AS VARIÁVEIS QUE ESTÃO VINDO DO BACK-END
  data() {
    return {
      usuarios: [],
      usuariosLoading: true,
      usuariosSelecao: [],
      filtroUsuarios: null,
      usuarioConfig: [],
      empresas: [],
      empresaVisible: false,
      empresasData: [],
      empresaxMoeda: [],
      link: "",
      consdataInsereV: false,
      consdataUpdateV: false,
      consdata: [],
    };
  },
  methods: {

    insereCadastro() {
      //INSERE NO BANCO
      axios
      // conecta com o back
        .post(
          `${process.env.VUE_APP_API}/Cadastro/createCadastro`,
          {
            idt_empresa: this.codEmpr,
            desc_empresa: this.descEmpr,
            tipo_empresa: this.tipoEmpr,
          },
          {
            headers: {
              Authorization: `Bearer ${this.state.user.token}`,
            },
          }
        )
        .then(() => {
            this.empresasData.push({"Nome": this.codEmpr, "Email": this.descEmpr, "Curso": this.tipoEmpr})
          helper.showSnackbar("Empresa Inserida");
        })
        .catch(() => {
          helper.showSnackbar("Não foi possível inserir a Empresa.");
        });
    },
  },
  computed: {
    state: () => store.state,
  },
};
</script> -->