<template>
  <v-container>
    <v-layout justify-center>
      <v-flex md6>
        <h1>Login</h1><hr>
        <v-flex xs12>
          <v-text-field
            v-model="user.username"
            name="username"
            v-validate="'required'"
            :error-messages="errors.collect('username')"
            label="email"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field
            v-model="user.password"
            name="password"
            v-validate="'required|min:8'"
            :error-messages="errors.collect('password')"
            label="password"
            type="password"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-btn
            color="primary"
            @click="loginUser"
          >
            LogIn
          </v-btn>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./Login.js"></script>