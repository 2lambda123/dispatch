<template>
  <div v-if="items.length">
    <new-edit-sheet />
    <v-divider />
    <v-list>
      <v-list-group prepend-icon="mdi-book-outline" color="info">
        <template #activator="{ props }">
          <v-list-item v-bind="props">
            <v-list-item-title>Definitions ({{ items.length }})</v-list-item-title>
          </v-list-item>
        </template>
        <v-list-item
          v-for="item in items"
          :key="item.content.id"
          @click="createEditShow(item.content)"
        >
          <v-list-item-title>{{ item.content.text }}</v-list-item-title>
          <v-list-item-subtitle>Text</v-list-item-subtitle>
        </v-list-item>
      </v-list-group>
    </v-list>
  </div>
</template>
<script>
import { mapActions } from "vuex"
import NewEditSheet from "@/definition/NewEditSheet.vue"
export default {
  name: "DefinitionList",

  components: {
    NewEditSheet,
  },

  props: {
    items: {
      default: null,
      type: Array,
    },
  },

  methods: {
    ...mapActions("definition", ["createEditShow"]),
  },
}
</script>
