


import { extend } from 'vee-validate';
import { required, email, min } from 'vee-validate/dist/rules';

extend("required", {
  ...required,
  message: "This field is required"
});

extend('email', email);
extend('min', min);
