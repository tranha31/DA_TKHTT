<template>
  <div class="item-cbb">
    <span>{{ item }}</span>
    <div v-if="canEditing">
      <input
          :type="inputType"
          v-model="input"
          :placeholder="placeholder"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "InputInfoTemplate",
  props: {
    item: {
      required: true
    },
    canEditing: {
      type: String,
      default: "true"
    },
    visible: {
      type: Boolean,
      default: true
    },
    label: {
      type: String,
      default: ''
    },
    inputType: {
      type: String,
      default: 'text'
    },
    placeholder: {
      type: String,
      default: ''
    },
    isValid: {
      type: Boolean,
      default: true
    },
    mandatory: {
      type: Boolean,
      default: false
    },
    value: {
      type: [String, Number],
      default: ''
    },
    isOnlyAlpha: {
      type: Boolean,
      default: true
    },
    isOnlyNumeric: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    valid() {
      return this.isValid
    },
    input: {
      get() {
        if (this.isOnlyAlpha) {
          let checkedText = this.value !== null ? this.value.replace(/[a-zA-Z]+/g, '') : this.value
          return checkedText
        } else if (this.isOnlyNumeric) {
          let checkedText = this.value !== null ? this.value.replace(/[0-9]+/g, '') : this.value
          return checkedText
        }
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      }
    }
  },
  methods: {

  }
}
</script>

<style>
.item-cbb{
  height: 32px;
  padding: 16px 0px 6px 20px;
  margin-bottom: 40px;
}

.item-cbb span {
  font-size: 16px;
}


</style>