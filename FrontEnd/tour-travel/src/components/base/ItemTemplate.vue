<template>
    <div class="item-cbb">
        <span>{{ item }}</span>
    </div>
</template>

<script>
export default {
    name: "ItemTemplate",
    props:{
        item:{ required: true },

    }
}
</script>

<style>
    .item-cbb{
        height: 32px;
        padding: 6px 0px 6px 10px;
    }
    .item-cbb:hover{
        background-color: #ebedf0 !important;
    }
    
    .item-cbb:hover span{
        color: #2ca01c !important;
    }

    .item-choose{
        color: #ffffff !important;
        background-color: #2ca01c !important;
    }

    
</style>