<template>
  <transition name="modal">
    <div class="modal-mask" @click.self="$emit('background')">
      <div class="modal-wrapper" v-click-outside="clickedOutside">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header"></slot>
          </div>

          <div class="modal-body">
            <slot name="body"></slot>
          </div>

          <div class="modal-footer">
            <slot name="footer"></slot>
            <button
                v-for="action in actions"
                :class="[
                action.css ? action.css : '',
                actionLoading === action.id ? 'is-loading' : ''
              ]"
                :key="action.id"
                @click="$emit(action.id)"
                class="button is-normal is-blue"
            >
              {{ action.label }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    actions: {
      type: Array,
      default: function() {
        return [
          {
            id: 'close',
            label: 'CLOSE'
          }
        ]
      }
    },
    actionLoading: String
  },
  data() {
    return {}
  },
  methods: {
    clickedOutside() {
      this.$emit('close')
    }
  }
}
</script>

<style>
@import url(../../css/common/modal.css);
</style>
