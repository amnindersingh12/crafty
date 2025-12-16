from django.core.management.base import BaseCommand
from core.models import Category, Product


class Command(BaseCommand):
    help = 'Load sample product data'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Crochet', 'slug': 'crochet'},
            {'name': 'Knitting', 'slug': 'knitting'},
            {'name': 'Sewing', 'slug': 'sewing'},
            {'name': 'Journaling', 'slug': 'journaling'},
            {'name': 'Needlepoint', 'slug': 'needlepoint'},
            {'name': 'Clay', 'slug': 'clay'},
            {'name': 'Painting', 'slug': 'painting'},
        ]
        
        for cat_data in categories_data:
            Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(categories_data)} categories'))
        
        
        # Create products with diverse crafting items
        products_data = [
            # Crochet Products
            {
                'name': 'Lavender Dream Blanket',
                'slug': 'lavender-dream-blanket',
                'description': 'A soft, handcrafted crochet blanket in beautiful lavender tones. Perfect for cozy evenings. Made with premium cotton yarn for lasting comfort.',
                'price': 89.99,
                'category': 'crochet',
                'featured': True,
            },
            {
                'name': 'Amigurumi Bunny',
                'slug': 'amigurumi-bunny',
                'description': 'Adorable handmade crochet bunny. The perfect gift for little ones or collectors. Each one is unique and made with love.',
                'price': 32.00,
                'category': 'crochet',
                'featured': False,
            },
            {
                'name': 'Boho Crochet Wall Hanging',
                'slug': 'boho-crochet-wall-hanging',
                'description': 'Stunning macramé-style wall art with intricate crochet patterns. Adds a bohemian touch to any room.',
                'price': 65.00,
                'category': 'crochet',
                'featured': True,
            },
            {
                'name': 'Crochet Market Bag',
                'slug': 'crochet-market-bag',
                'description': 'Eco-friendly reusable market bag with sturdy handles. Perfect for shopping or beach trips.',
                'price': 28.00,
                'category': 'crochet',
                'featured': False,
            },
            
            # Knitting Products
            {
                'name': 'Cozy Cable Knit Scarf',
                'slug': 'cozy-cable-knit-scarf',
                'description': 'Classic cable knit pattern in soft merino wool. Warm and stylish for the colder months. Available in multiple colors.',
                'price': 45.00,
                'category': 'knitting',
                'featured': True,
            },
            {
                'name': 'Chunky Knit Beanie',
                'slug': 'chunky-knit-beanie',
                'description': 'Warm and trendy chunky knit beanie. Made with super soft wool blend. One size fits most.',
                'price': 25.00,
                'category': 'knitting',
                'featured': False,
            },
            {
                'name': 'Hand-Knit Wool Mittens',
                'slug': 'hand-knit-wool-mittens',
                'description': 'Cozy mittens with Fair Isle patterns. Lined with soft fleece for extra warmth.',
                'price': 38.00,
                'category': 'knitting',
                'featured': False,
            },
            {
                'name': 'Knitted Baby Blanket',
                'slug': 'knitted-baby-blanket',
                'description': 'Soft and gentle baby blanket in pastel colors. Made with hypoallergenic yarn, perfect for newborns.',
                'price': 55.00,
                'category': 'knitting',
                'featured': True,
            },
            
            # Sewing Products
            {
                'name': 'Handmade Tote Bag',
                'slug': 'handmade-tote-bag',
                'description': 'Durable canvas tote bag with hand-sewn details. Perfect for everyday use, shopping, or trips to the farmer\'s market.',
                'price': 35.00,
                'category': 'sewing',
                'featured': True,
            },
            {
                'name': 'Quilted Makeup Pouch',
                'slug': 'quilted-makeup-pouch',
                'description': 'Hand-quilted makeup pouch with zipper closure. Water-resistant lining keeps your essentials organized.',
                'price': 22.00,
                'category': 'sewing',
                'featured': False,
            },
            {
                'name': 'Patchwork Throw Pillow',
                'slug': 'patchwork-throw-pillow',
                'description': 'Colorful patchwork cushion with vintage fabric scraps. Each pillow is one-of-a-kind.',
                'price': 42.00,
                'category': 'sewing',
                'featured': False,
            },
            {
                'name': 'Fabric Headband Set',
                'slug': 'fabric-headband-set',
                'description': 'Set of 3 handmade fabric headbands in coordinating patterns. Comfortable and stylish.',
                'price': 18.00,
                'category': 'sewing',
                'featured': False,
            },
            
            # Journaling Products
            {
                'name': 'Bullet Journal Starter Kit',
                'slug': 'bullet-journal-starter-kit',
                'description': 'Everything you need to start your journaling journey. Includes notebook, stickers, washi tape, and inspiration guide.',
                'price': 28.00,
                'category': 'journaling',
                'featured': True,
            },
            {
                'name': 'Washi Tape Collection',
                'slug': 'washi-tape-collection',
                'description': 'Set of 12 unique washi tapes in pastel colors. Perfect for journaling, scrapbooking, and crafts.',
                'price': 18.00,
                'category': 'journaling',
                'featured': False,
            },
            {
                'name': 'Watercolor Sticker Pack',
                'slug': 'watercolor-sticker-pack',
                'description': 'Hand-painted watercolor stickers featuring florals and nature themes. 50+ unique designs.',
                'price': 12.00,
                'category': 'journaling',
                'featured': False,
            },
            {
                'name': 'Leather Journal Cover',
                'slug': 'leather-journal-cover',
                'description': 'Handcrafted leather cover for standard notebooks. Ages beautifully with use.',
                'price': 48.00,
                'category': 'journaling',
                'featured': True,
            },
            
            # Needlepoint Products
            {
                'name': 'Floral Needlepoint Hoop',
                'slug': 'floral-needlepoint-hoop',
                'description': 'Delicate floral design on linen fabric. Comes framed in wooden embroidery hoop, ready to hang.',
                'price': 52.00,
                'category': 'needlepoint',
                'featured': True,
            },
            {
                'name': 'Custom Name Needlepoint',
                'slug': 'custom-name-needlepoint',
                'description': 'Personalized needlepoint with name or phrase of your choice. Perfect for nurseries or gifts.',
                'price': 68.00,
                'category': 'needlepoint',
                'featured': False,
            },
            
            # Clay Products
            {
                'name': 'Handmade Ceramic Mug',
                'slug': 'handmade-ceramic-mug',
                'description': 'Wheel-thrown ceramic mug with unique glaze. Microwave and dishwasher safe. Each piece is unique.',
                'price': 32.00,
                'category': 'clay',
                'featured': True,
            },
            {
                'name': 'Clay Plant Pot Set',
                'slug': 'clay-plant-pot-set',
                'description': 'Set of 3 terracotta pots with drainage holes. Hand-painted with geometric patterns.',
                'price': 45.00,
                'category': 'clay',
                'featured': False,
            },
            {
                'name': 'Polymer Clay Earrings',
                'slug': 'polymer-clay-earrings',
                'description': 'Lightweight statement earrings in modern abstract designs. Hypoallergenic posts.',
                'price': 24.00,
                'category': 'clay',
                'featured': False,
            },
            
            # Painting Products
            {
                'name': 'Abstract Canvas Art',
                'slug': 'abstract-canvas-art',
                'description': 'Original acrylic painting on stretched canvas. Vibrant colors and bold brushstrokes. 16x20 inches.',
                'price': 125.00,
                'category': 'painting',
                'featured': True,
            },
            {
                'name': 'Watercolor Landscape Print',
                'slug': 'watercolor-landscape-print',
                'description': 'High-quality print of original watercolor painting. Serene mountain landscape. 11x14 inches.',
                'price': 35.00,
                'category': 'painting',
                'featured': False,
            },
            {
                'name': 'Hand-Painted Wooden Sign',
                'slug': 'hand-painted-wooden-sign',
                'description': 'Rustic wooden sign with hand-lettered quote. Perfect for home decor.',
                'price': 42.00,
                'category': 'painting',
                'featured': False,
            },
        ]
        
        created_count = 0
        for prod_data in products_data:
            category = Category.objects.get(slug=prod_data['category'])
            _, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults={
                    'name': prod_data['name'],
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'category': category,
                    'featured': prod_data['featured'],
                }
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} products'))
