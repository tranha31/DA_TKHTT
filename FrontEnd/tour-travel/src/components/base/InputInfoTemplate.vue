<template>
  <div class="item-cbb" :style="{'margin-bottom': displayInline === 'block' ? '40px' : '32px'}">
    <span>{{ item }}</span>
    <div v-if="canEditing" :style="{'display':  displayInline }">
      <input
          :type="inputType"
          v-model="input"
          :placeholder="placeholder"
      />
    </div>
    <div v-else :style="{'display':  displayInline }">
      <input
          :type="inputType"
          v-model="input"
          disabled="true"
          :placeholder="value"
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
      type: Boolean,
      default: false
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
    },
    displayInline: {
      type: String,
      default: 'block'
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
}

.item-cbb div {
  width: 100%;
}

.item-cbb span {
  font-size: 16px;
  display: inline-block;
  width: 190px;
}


</style>