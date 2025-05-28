<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Select Inputs">
          <SelectInput />
        </ComponentCard>
        <ComponentCard title="Inputs States">
          <TextArea />
        </ComponentCard>

      </div>
      <div class="space-y-6">
        <ComponentCard title="File Input"> <FileInput /> </ComponentCard>
        <ComponentCard title="Checkboxes">
          <CheckboxInput />
        </ComponentCard>
        <ComponentCard title="Dropzone">
          <Dropzone />
        </ComponentCard>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import SelectInput from '@/components/Muestras/FormElements/SelectInput.vue'
import TextArea from '@/components/Muestras/FormElements/TextArea.vue'
import Dropzone from '@/components/Muestras/FormElements/Dropzone.vue'
import FileInput from '@/components/Muestras/FormElements/FileInput.vue'
import CheckboxInput from '@/components/Muestras/FormElements/CheckboxInput.vue'

const currentPageTitle = ref('Form Elements')
</script>
